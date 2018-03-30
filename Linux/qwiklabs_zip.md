# scripts

## Linux scripts

## **Qwiklabs zip**


In order to save a qwiklab lesson, do these steps:

### 1. Check if zip/unzip installed
```bash
!command -v zip
!command -v unzip
```
Output:
> /usr/bin/zip  
> /usr/bin/unzip

Alternatively, check if `tar` is installed. At least `tar` should be available by default:
```bash
!command -v tar
```
Output:
> /bin/tar

### 2. Check current folder
Usually you would be in `/home/ubuntu`, `/home/<user>`, `/notebooks`:
```bash
!pwd
```
Output:
> /home/ubuntu/lesson

If you're in a subfolder, you should perform step 3 for all levels below `/home/<user>` folder.

### 3. Check folder size / check files (recurse)
Lists folder size and files:
```bash
!du -sh ./
!ls -lh ./
```
Output:
> 3M  ./
> total 3M
> -rw-rw-r--  <...>


### 4. Compress files and download from Jupyter/IPython interface
Zip files (`-r` for recursion, `--exclude` for file/folder exclusion, select files for zip):
```bash
!zip -r lesson.zip ./
```

Zip files with tar:
```bash
# trailing ./ is probably wrong ...
!tar -zcvf lesson.tar.gz ./
```

### Misc
+ save models from DIGITS
+ screenshots
+ complete html downloads + print as pdf
