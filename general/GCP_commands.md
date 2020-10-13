# scripts
## general / GCP_commands

### gcloud

When using Qwiklabs, check that user/project is ok:  
`gcloud auth list ; gcloud config list project`  
More details: `gcloud config list`

gcloud config get-value project
gcloud config set project [id]

```bash
gcloud services enable \
    cloudresourcemanager.googleapis.com\
    gkehub.googleapis.com\
    anthos.googleapis.com
```

### gsutil

`gsutil acl ch -u AllUsers:R gs://...`
