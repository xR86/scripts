# scripts

## Linux scripts

## **Google Colab setup**


In order to configure and save data from a Colab notebook, do these steps:

### 1. Update environment

```python
!apt-get install graphviz -qq
!pip install graphviz -q
!pip install pydot -q
# restart runtime
```

### 2. Save created files

```python
# single use
# from google.colab import files
# files.download('data.zip')

# Note: allow multiple downloads from the Chrome pop-up
def download_colab_files(file_lst):
    from google.colab import files
    
    print('Downloading: %s' % file_lst)
    for file in file_lst:
        files.download(file)

# download_colab_files(['model.json', 'model_weights.h5'])
```

You can also save colab config files before starting anything:  
`ls -la > list_ls.txt`  
`!zip -r data.zip ./ -x "datalab/*" ".forever/sock/*" ".cache/*" ".keras/datasets/*" ".keras/models/*"`


### Misc
+ save notebook and download
