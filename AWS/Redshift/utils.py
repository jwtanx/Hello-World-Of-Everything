import redshift_connector


def get_connection():

    workgroup = 'workgroup-name'
    account_id = '123456789'
    region = 'ap-southeast-1'

    conn = redshift_connector.connect(
        credentials_provider='BrowserIdcAuthPlugin',
        host=
        f'{workgroup}.{account_id}.{region}.redshift-serverless.amazonaws.com',
        database='dev',
        idc_region=region,
        issuer_url='https://company-sso.awsapps.com/start',
        idp_response_timeout=20,
        is_serverless=True,
        listen_port=5439,
        idc_client_display_name='redshift-idc-app',
    )

    return conn


if __name__ == '__main__':
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute('SELECT TOP 1 FROM schema.table')
        result = cursor.fetchall()
        print(result)
    except redshift_connector.error.ProgrammingError as exception:
        print(dict(exception.args[0]).get('M'))
        conn.close()
