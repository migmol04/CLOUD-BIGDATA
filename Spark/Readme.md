# Spark with Google Cloud Dataproc and Cloud Storage

## 📖 Introduction

Apache Spark is a distributed processing framework designed for large-scale data. By combining **Google Cloud Storage** with **Google Cloud Dataproc**, you can decouple storage from compute resources, enabling a scalable and efficient solution.

This repository provides instructions for running a Spark job using Cloud Storage for input and output.

---

## Prerequisites

1. **Google Cloud Storage Bucket**:
   - Create a bucket in Google Cloud Storage to store input and output files (e.g., `gs://your-bucket-name`).

2. **Google Cloud Dataproc Cluster**:
   - A Dataproc cluster with Spark installed.

3. **Job Files**:
   - Spark scripts in Python or Scala (`job.py` or `job.scala`) to process the data.

---

## Running the Spark Job

### Step 1: Upload Files to the Cloud Storage Bucket

Replace `$BUCKET_NAME` with your bucket name:

```bash
BUCKET=gs://$BUCKET_NAME
gsutil cp input_data/* $BUCKET/input/
```

### Step 2: Submit the Job to Spark on Dataproc

Submit the Spark job to your cluster using the `gcloud` command. Depending on the language, use the following commands:

#### **For Python**
```bash
gcloud dataproc jobs submit pyspark job.py \
    --cluster=$CLUSTER_NAME \
    --region=$REGION \
    --jars file:///usr/lib/spark/external/spark-avro.jar \
    -- $BUCKET/input/ $BUCKET/output/
```

### Step 3: Check the Output

Once the job is complete, the results will be stored in the specified bucket.

1. **List the output files:**
   ```bash
   gcloud storage ls -l $BUCKET/output/
   ```
2.  **View the Output File Contents:**
To view the contents of the output files, use the following command:

```
```bash
gcloud storage cat $BUCKET/output/* | more
```

### Notes

1. **Storage Decoupling**:
   - Using Cloud Storage ensures that data remains available even after deleting the Dataproc cluster.

2. **Overwrite Prevention**:
   - Ensure that the output folder does not exist in the bucket before running the job; otherwise, Spark will raise an error.

3. **Resource Optimization**:
   - You can adjust the cluster size and the number of worker nodes to optimize job performance.

