FILESEXTRAPATHS:prepend := "${THISDIR}/files:"

SRC_URI += "file://mosquitto.conf"

do_install:append() {
    install -d ${D}${sysconfdir}/mosquitto
    install -m 0644 ${WORKDIR}/mosquitto.conf ${D}${sysconfdir}/mosquitto/mosquitto.conf
    install -d ${D}/var/lib/mosquitto
}

# Adiciona a pasta criada à lista de arquivos do pacote principal
FILES:${PN} += "/var/lib/mosquitto"
