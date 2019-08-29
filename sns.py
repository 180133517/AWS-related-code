import boto3

sns=boto3.client('sns')

topic_list=['test1','test2','test3','test4']
email_list=['leo.leung@nextlink.com.hk']
topic_arn=[]

for topic in topic_list:
    craete_topic=sns.create_topic(Name=topic)

arn=sns.list_topics()
topics = [topic['TopicArn'] for topic in arn['Topics']]
topic_arn.append(topics)
for arn in topic_arn:
    for email in email_list:
        subscribe=sns.subscribe(TopicArn=arn,Protocol='email',Endpoint=email)

