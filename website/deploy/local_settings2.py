from __future__ import unicode_literals

SECRET_KEY = "%(secret_key)s"
NEVERCACHE_KEY = "%(nevercache_key)s"

# Domains for public site
ALLOWED_HOSTS = ["localhost",
		"188.166.161.103",
		"127.0.0.1"]

FABRIC = {
		    "DEPLOY_TOOL": "git",  # Deploy with "git", "hg", or "rsync"
		        "SSH_USER": "root",  # VPS SSH username
			    "HOSTS": ["123.123.123.123"],  # The IP address of your VPS
			        "DOMAINS": ALLOWED_HOSTS,  # Edit domains in ALLOWED_HOSTS
				    "REQUIREMENTS_PATH": "requirements.txt",  # Project's pip requirements
				        "LOCALE": "en_US.UTF-8",  # Should end with ".UTF-8"
					    "DB_PASS": "",  # Live database password
					        "ADMIN_PASS": "",  # Live admin user password
						    "SECRET_KEY": SECRET_KEY,
						        "NEVERCACHE_KEY": NEVERCACHE_KEY,
							}

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        # DB name or path to database file if using sqlite3.
        "NAME": "%(proj_name)s",
        # Not used with sqlite3.
        "USER": "%(proj_name)s",
        # Not used with sqlite3.
        "PASSWORD": "%(db_pass)s",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "127.0.0.1",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTOCOL", "https")

CACHE_MIDDLEWARE_SECONDS = 60

CACHE_MIDDLEWARE_KEY_PREFIX = "%(proj_name)s"

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.memcached.MemcachedCache",
        "LOCATION": "127.0.0.1:11211",
    }
}

SESSION_ENGINE = "django.contrib.sessions.backends.cache"




