import boto3

sns=boto3.client('sns')
cloudwatch=boto3.client('cloudwatch')

topic_list=['test1','test2','test3','test4']
email_list=['leo.leung@nextlink.com.hk']
topic_arn=['arn:aws:sns:us-east-2:290455323267:test1', 'arn:aws:sns:us-east-2:290455323267:test2', 'arn:aws:sns:us-east-2:290455323267:test3', 'arn:aws:sns:us-east-2:290455323267:test4']
name=['cpu','ram','speed','disk']
metric=['CPUUtilization','NetworkIn','NetworkOut','DiskWriteOps']

for n in name:
    for m in metric:
        cloudwatch.put_metric_alarm(
        MetricName=,
        AlarmName=n,
        ComparisonOperator='GreaterThanThreshold',
        EvaluationPeriods=1,
        Namespace='AWS/EC2',
        Period=60,
        Statistic='Average',
        Threshold=70.0,
        ActionsEnabled=False,
        AlarmDescription='Alarm when server CPU exceeds 70%')
