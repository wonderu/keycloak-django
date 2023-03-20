# keycloak-django

Example of authenticating Django with Keycloak

based on tutorial <https://number1.co.za/using-keycloak-as-the-identity-provider-for-users-on-django-and-django-admin/>

python3.10 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt

Add
127.0.0.1 keycloak
to /etc/hosts/
