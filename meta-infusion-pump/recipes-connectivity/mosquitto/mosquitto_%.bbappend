FILESEXTRAPATHS:prepend := "${THISDIR}/files:"

SRC_URI:append = " file://mosquitto.conf"

# Sobrescreve o arquivo de configuração padrão pelo nosso
do_install:append() {
    install -d ${D}${sysconfdir}/mosquitto
    install -m 0644 ${WORKDIR}/mosquitto.conf ${D}${sysconfdir}/mosquitto/mosquitto.conf
}
