# MapReduce with Google Cloud Dataproc and Cloud Storage

## Introduction
**MapReduce** is a programming model designed for processing and generating large datasets. By using **Google Cloud Storage** in combination with **Google Cloud Dataproc**, we can decouple storage from compute resources, enabling efficient and scalable data processing.

This repository provides instructions for running a MapReduce job using Cloud Storage for input and output.

---

## Prerequisites
1. A **Google Cloud Storage** bucket (e.g., `gs://your-bucket-name`) to store input and output files.
2. A **Google Cloud Dataproc** cluster already created.

---

## Running the MapReduce Job

### **Step 1: Upload Files to Cloud Storage**
1. Replace `$BUCKET_NAME` with the name of your Cloud Storage bucket:
   ```bash
   BUCKET=gs://$BUCKET_NAME
    ```

### Step 2: Submit the Job
Run the following command from the master node of your Dataproc cluster to submit the MapReduce job:

```bash
mapred streaming -files mapper.py,reducer.py -mapper mapper.py \
-reducer reducer.py -input $BUCKET/input -output $BUCKET/output
 ```

### Step 3: Check the Output
After the job completes, verify the results stored in Cloud Storage.

#### List the output files:
```bash
gcloud storage ls -l $BUCKET/output
 ```

#### View the contents of the output files:
```bash
gcloud storage cat $BUCKET/output/* | more
 ```

### Notes
- **Storage Decoupling**: Using Cloud Storage allows you to delete the cluster once processing is complete while preserving the data for future use.
- **Overwrite Prevention**: Ensure the output folder does not already exist in the bucket; otherwise, the job will fail.
