# Liste der Dienstnamen
service_list = [
    "adguardhome-sync",
    "airsonic-advanced",
    "altus",
    "apprise-api",
    "audacity",
    "babybuddy",
    "bambustudio",
    "bazarr",
    "beets",
    "blender",
    "boinc",
    "booksonic-air",
    "bookstack",
    "budge",
    "calibre-web",
    "calibre",
    "calligra",
    "changedetection.io",
    "chromium",
    "code-server",
    "cops",
    "cura",
    "daapd",
    "darktable",
    "davos",
    "ddclient",
    "deluge",
    "digikam",
    "dillinger",
    "diskover",
    "dokuwiki",
    "domoticz",
    "doplarr",
    "doublecommander",
    "duckdns",
    "duplicati",
    "emby",
    "embystat",
    "emulatorjs",
    "endlessh",
    "fail2ban",
    "faster-whisper",
    "feed2toot",
    "ferdium",
    "ffmpeg",
    "filezilla",
    "firefox",
    "fleet",
    "flexget",
    "foldingathome",
    "freecad",
    "freshrss",
    "gimp",
    "github-desktop",
    "gitqlient",
    "grav",
    "grocy",
    "habridge",
    "headphones",
    "healthchecks",
    "hedgedoc",
    "heimdall",
    "hishtory-server",
    "homeassistant",
    "htpcmanager",
    "inkscape",
    "jackett",
    "jellyfin",
    "kasm",
    "kavita",
    "kdenlive",
    "kicad",
    "kimai",
    "krita",
    "lazylibrarian",
    "ldap-auth",
    "libreoffice",
    "librespeed",
    "lidarr",
    "limnoria",
    "lollypop",
    "lychee",
    "mariadb",
    "mastodon",
    "mediaelch",
    "medusa",
    "minetest",
    "minisatip",
    "mstream",
    "mullvad-browser",
    "mylar3",
    "mysql-workbench",
    "nano-wallet",
    "nano",
    "netbootxyz",
    "netbox",
    "nextcloud",
    "nginx",
    "ngircd",
    "nzbhydra2",
    "ombi",
    "openssh-server",
    "openvscode-server",
    "opera",
    "orcaslicer",
    "oscam",
    "overseerr",
    "pairdrop",
    "phpmyadmin",
    "pidgin",
    "piper",
    "piwigo",
    "plex-meta-manager",
    "plex",
    "projectsend",
    "prowlarr",
    "pwndrop",
    "pydio-cells",
    "pyload-ng",
    "pylon",
    "qbittorrent",
    "qdirstat",
    "quassel-core",
    "quassel-web",
    "radarr",
    "raneto",
    "rdesktop",
    "readarr",
    "remmina",
    "resilio-sync",
    "rsnapshot",
    "sabnzbd",
    "series-troxide",
    "sickchill",
    "sickgear",
    "smokeping",
    "snapdrop",
    "snipe-it",
    "sonarr",
    "sqlitebrowser",
    "steamos",
    "swag",
    "synclounge",
    "syncthing",
    "syslog-ng",
    "tautulli",
    "thelounge",
    "transmission",
    "tvheadend",
    "ubooquity",
    "unifi-controller",
    "unifi-network-application",
    "vscodium",
    "webcord",
    "webgrabplus",
    "webtop",
    "wikijs",
    "wireguard",
    "wireshark",
    "wps-office",
    "xbackbone",
    "your_spotify",
    "znc"
]

# Pfad zum aktuellen Verzeichnis
current_directory = "./"

# Schleife über die Liste und Erstellen der .bash-Dateien
for service_name in service_list:
    file_name = f"{service_name}.bash"
    file_path = current_directory + file_name

    # Inhalt der .bash-Datei
    file_content = f"""#!/bin/bash

# Bash-Datei für {service_name}
# Fügen Sie hier Ihre Befehle für den Dienst {service_name} hinzu.

"""

    # .bash-Datei erstellen
    with open(file_path, "w") as bash_file:
        bash_file.write(file_content)

    print(f"Die Datei '{file_name}' wurde erstellt.")

print("Alle .bash-Dateien wurden erfolgreich erstellt.")
