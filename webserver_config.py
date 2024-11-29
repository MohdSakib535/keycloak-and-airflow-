from flask_appbuilder.security.manager import AUTH_OID

# Set authentication type to OpenID Connect
AUTH_TYPE = AUTH_OID

# OpenID Connect configuration
OIDC_CLIENT_SECRETS = '/opt/airflow/oidc_client_secrets.json'
OIDC_SCOPES = ['openid', 'email', 'profile']
OIDC_INTROSPECTION_ENDPOINT = 'http://keycloak:8080/realms/master/protocol/openid-connect/token/introspect'
OIDC_USER_INFO_ENDPOINT = 'http://keycloak:8080/realms/master/protocol/openid-connect/userinfo'

# Enable user registration
AUTH_USER_REGISTRATION = True
AUTH_USER_REGISTRATION_ROLE = "Admin"  # Default role for new users

# Define OpenID Providers
OPENID_PROVIDERS = [{
    'name': 'keycloak',
    'icon': 'fa-user-circle',
    'token_key': 'access_token',
    'remote_app': {
        'client_id': 'airflow-client',
        'client_secret': 'etg39LK5iEtQzUzK8MPePeD7juLwJB7D',
        'api_base_url': 'http://localhost:8080/realms/master/protocol/openid-connect',
        'client_kwargs': {
            'scope': 'openid email profile'
        },
        'access_token_url': 'http://keycloak:8080/realms/master/protocol/openid-connect/token',
        'authorize_url': 'http://keycloak:8080/realms/master/protocol/openid-connect/auth',
        'request_token_url': None
    }
}]





# from airflow.configuration import conf

# # Import OIDC-related classes
# from flask_appbuilder.security.manager import AUTH_OID
# from flask_oidc import OpenIDConnect

# # Configure the authentication backend
# AUTH_TYPE = AUTH_OID

# # OIDC Configuration
# OIDC_CLIENT_SECRETS = conf.get("webserver", "OIDC_CLIENT_SECRETS")
# OIDC_SCOPES = conf.get("webserver", "OIDC_SCOPES")
# OIDC_OPENID_REALM = 'airflow'

# # Security Manager Overrides (if necessary)
# # You might need to create a custom Security Manager if default OIDC does not suffice
