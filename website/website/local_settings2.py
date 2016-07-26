from __future__ import unicode_literals


# Domains for public site
ALLOWED_HOSTS = ["localhost",
		"188.166.161.103",
		"127.0.0.1"]

FABRIC = {
		    "DEPLOY_TOOL": "git",  # Deploy with "git", "hg", or "rsync"

#    "VIRTUALENV_HOME":  "/home/moritz", # Absolute remote path for virtualenvs
		        "SSH_USER": "moritz",  # VPS SSH username
			"HOSTS": ["188.166.161.103"],  # The IP address of your VPS
			        "DOMAINS": ALLOWED_HOSTS,  # Edit domains in ALLOWED_HOSTS
				    "REQUIREMENTS_PATH": "requirements.txt",  # Project's pip requirements
				        "LOCALE": "en_US.UTF-8",  # Should end with ".UTF-8"
					    "DB_PASS": "you shall not pass",  # Live database password
					        "ADMIN_PASS": "",  # Live admin user password
						    "SECRET_KEY": "eqd%4#m!282ncx@x+=mv=)fpiu@@box^+hh^h_2%%w=+5md6+2",
						        "NEVERCACHE_KEY": "giw$pg3l&jwvhjx!814tg(cd=k2*9k9df_sek9bll3zwn!9r*v",
							}

#FABRIC = {
 #   "PROJECT_NAME": "do_test", # Unique identifier for project
 #   "LIVE_HOSTNAME": "do.bitpl.us", # Host for public site.
 #   "REPO_URL": "https://joshcartme@bitbucket.org/joshcartme/vanilla_mezz", # Git or Mercurial remote repo URL for the project
#}


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




