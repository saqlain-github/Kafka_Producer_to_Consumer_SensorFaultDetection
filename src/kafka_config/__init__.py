
import os

'''
SECURITY_PROTOCOL="SASL_SSL"
SSL_MACHENISM="PLAIN"
API_KEY = os.getenv('API_KEY',None)
ENDPOINT_SCHEMA_URL  = os.getenv('ENDPOINT_SCHEMA_URL',None)
API_SECRET_KEY = os.getenv('API_SECRET_KEY',None)
BOOTSTRAP_SERVER = os.getenv('BOOTSTRAP_SERVER',None)
SECURITY_PROTOCOL = os.getenv('SECURITY_PROTOCOL',None)
SSL_MACHENISM = os.getenv('SSL_MACHENISM',None)
SCHEMA_REGISTRY_API_KEY = os.getenv('SCHEMA_REGISTRY_API_KEY',None)
SCHEMA_REGISTRY_API_SECRET = os.getenv('SCHEMA_REGISTRY_API_SECRET',None)
'''

SECURITY_PROTOCOL="SASL_SSL" #Simple Auth and Security layer - connect securely
SSL_MACHENISM="PLAIN"

#API Details
API_KEY = "COW5763J2HJXHT7E" #os.getenv('API_KEY',None)
API_SECRET_KEY = "rWe19ZGl0FZZRh4jmk9XLetDeDzDFFpZkBEX+xNHnHLrx3E3wMdZrJgay04K5iyJ" # os.getenv('API_SECRET_KEY',None)
BOOTSTRAP_SERVER = "pkc-41p56.asia-south1.gcp.confluent.cloud:9092" #os.getenv('BOOTSTRAP_SERVER',None)

# Schema Related Cred
ENDPOINT_SCHEMA_URL  = "https://psrc-znpo0.ap-southeast-2.aws.confluent.cloud" #os.getenv('ENDPOINT_SCHEMA_URL',None)
SCHEMA_REGISTRY_API_KEY = "56HGY64GFCDTVH73" #os.getenv('SCHEMA_REGISTRY_API_KEY',None)
SCHEMA_REGISTRY_API_SECRET = "VTWaZjmR7nn8bD6HvxDBydlP2/N2oq+BVDOlvoM6EFPDx2+CUPgSAI6Pm478iNkI" #os.getenv('SCHEMA_REGISTRY_API_SECRET',None)

def sasl_conf():

    sasl_conf = {'sasl.mechanism': SSL_MACHENISM,
                 # Set to SASL_SSL to enable TLS support.
                #  'security.protocol': 'SASL_PLAINTEXT'}
                'bootstrap.servers':BOOTSTRAP_SERVER,
                'security.protocol': SECURITY_PROTOCOL,
                'sasl.username': API_KEY,
                'sasl.password': API_SECRET_KEY
                }
    print(sasl_conf)
    return sasl_conf



def schema_config():
    return {'url':ENDPOINT_SCHEMA_URL,
    
    'basic.auth.user.info':f"{SCHEMA_REGISTRY_API_KEY}:{SCHEMA_REGISTRY_API_SECRET}"

    }

if __name__ == '__main__':
    sasl_conf()

