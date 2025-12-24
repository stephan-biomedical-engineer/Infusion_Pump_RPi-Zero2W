FILESEXTRAPATHS:prepend := "${THISDIR}/files:"

SRC_URI += "file://25-wlan.network"

do_install:append() {
    # Instala a configuração de rede do Systemd
    install -d ${D}${sysconfdir}/systemd/network
    install -m 0644 ${WORKDIR}/25-wlan.network ${D}${sysconfdir}/systemd/network/
}

FILES:${PN} += "${sysconfdir}/systemd/network"
