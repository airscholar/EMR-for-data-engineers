"""

ssh -i [key-pair] hadoop@[emr-master-public-dns-address]

nano spark-etl.py

spark-submit spark-etl.py s3://<YOUR-BUCKET>/input/ s3://<YOUR-BUCKET>/output/spark


spark-submit s3://<bucketname>/files/spark-etl.py s3://<bucketname>/input s3://<bucketname>/output


"""