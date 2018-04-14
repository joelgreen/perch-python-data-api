from perch.private import default_aws_access_key_id, default_aws_secret_access_key

default_aws_region = "us-west-2"


class Default(object):
    # AWS Credentials
    aws_access_key_id = default_aws_access_key_id
    aws_secret_access_key = default_aws_secret_access_key

    aws_region = default_aws_region

    # Elasticsearch URL
    elasticsearch_host_url = "search-perch-pla2or76rhkktulwix6unxknce.us-west-2.es.amazonaws.com"


env_mapper = {
    'default': Default
}

# What default environment everything should run on
env = Default
