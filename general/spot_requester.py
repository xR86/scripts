import datetime as dt
import json
import os
import subprocess as sp
import sys
import time

import boto3

ec2 = boto3.client('ec2', region_name='us-east-1')


def json_serial(obj):
	"""JSON serializer for objects not serializable by default json code"""

	if isinstance(obj, (dt.datetime, dt.date)):
		return obj.isoformat()
	raise TypeError ("Type %s not serializable" % type(obj))

def create_ssh_key(folder='~/.ssh/', key_name='aws_auto.key'):
	import os

	ssh_loc = os.path.expanduser('~/.ssh/')
	path = os.path.expanduser(folder) + key_name

	cmd = "ssh-keygen -t rsa -N "" -f %s" % path
	root, dirs, files = os.walk(ssh_loc).__next__()
	logger('Files found: \n%s' % files)

	if key_name not in files:
		cmd_split = cmd.split(" ")
		print('running %s as: %s' % 
			(cmd, cmd_split)
		)
		res = sp.run(cmd_split,
			stdout=sp.PIPE,
			check=True
		)
		logger('Subprocess returned code: %s' % res.returncode)
		logger('Subprocess stdout: \n%s' % res.stdout)
		logger('Subprocess stderr: \n%s' % res.stderr)
	else:
		logger('Key already saved')

def create_aws_key(key_name='aws_auto'):
	logger('Creating AWS Key')
	response = ec2.create_key_pair(KeyName=key_name)

	if response['ResponseMetadata']['HTTPStatusCode'] == 200:
		logger('Saving keypair to pem')
		with open('aws_auto.pem', 'w') as f:
			f.write(response['KeyMaterial'])
	else:
		logger('Keypair create response != 200')

def get_ssh_key(folder='~/.ssh/', key_name='aws_auto.pem'):
	ssh_loc = os.path.expanduser('~/.ssh/')
	return os.path.expanduser(folder) + key_name

def request_ze_spot_sir():
	test_dryrun = False

	req = ec2.request_spot_instances(
		DryRun = test_dryrun,
		SpotPrice = '0.01',
		ClientToken = 'string',
		InstanceCount=1,
		Type='one-time',
		LaunchSpecification={
			'ImageId': 'ami-66506c1c', # Ubuntu 16.04 LTS
			'KeyName': 'aws_auto',
			'SecurityGroups': ['dev-compute'], # use name, not ID
			'InstanceType': 't3.micro',
			'Placement': {
				'AvailabilityZone': 'us-east-1a',
			},
			'BlockDeviceMappings': [
				 {
                    "DeviceName": "/dev/sda1",
                    "Ebs": {
                        "DeleteOnTermination": True,
                        "Encrypted": False,
                        "VolumeSize": 20,
                        "VolumeType": "gp2"
                    }
                },
                {
                    "DeviceName": "/dev/sdb",
                    "VirtualName": "ephemeral0"
                },
                {
                    "DeviceName": "/dev/sdc",
                    "VirtualName": "ephemeral1"
                }

			],
			'EbsOptimized': True,
			'Monitoring': {
				'Enabled': True
			},
		}
	)


	logger(json.dumps(req, sort_keys=True, indent=4, separators=(',', ': '), default=json_serial))
	# print(req['SpotInstanceRequests'][0]['State'])
	
	status = req['SpotInstanceRequests'][0]['State']
	reqid = req['SpotInstanceRequests'][0]['SpotInstanceRequestId']
	logger('Spot request created, status: %s' % status)

	logger('Waiting for spot provisioning')
	while True:
		current_req = ec2.describe_spot_instance_requests(DryRun=False, SpotInstanceRequestIds = [reqid])
		status = current_req['SpotInstanceRequests'][0]['State']
		if status == 'active':
			logger('Provisioned')
			# instance = ec2.get_all_instances([current_req['SpotInstanceRequests'][0].SpotInstanceRequestId])[0].instances[0]
			# instance.add_tag('Name', 'test')
			response = ec2.describe_instances(
					Filters=[
						{
							'Name': 'key-name',
							'Values': [
								'aws_auto',
							]
						}
					],
					DryRun=False
			)
			logger(json.dumps(response, sort_keys=True, indent=4, separators=(',', ': '), default=json_serial))
		else:
			logger(json.dumps(current_req, sort_keys=True, indent=4, separators=(',', ': '), default=json_serial))

		print('.')
		time.sleep(1)


if __name__ == '__main__':
	print('\n')
	# create_ssh_key()
	# create_aws_key()
	print('\n')
	request_ze_spot_sir()

	# log = ec2.describe_spot_instance_requests(DryRun=False, SpotInstanceRequestIds = ['sir-k6yr4w6g'])
	# logger(json.dumps(log, sort_keys=True, indent=4, separators=(',', ': '), default=json_serial))
