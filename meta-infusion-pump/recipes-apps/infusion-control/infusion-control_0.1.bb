SUMMARY = "Software de Controle da Bomba de Infusão"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${COMMON_LICENSE_DIR}/MIT;md5=0835ade698e0bcf8506ecda2f7b4f302"

# Define que precisamos do Python e das libs
RDEPENDS:${PN} = "python3 python3-paho-mqtt rpi-gpio"

# Onde estão os arquivos fontes (local)
SRC_URI = " \
    file://listener.py \
    file://infusion-pump-init \
"

S = "${WORKDIR}"

# Instalação no sistema final
do_install() {
    # 1. Instala o script Python em /usr/bin
    install -d ${D}${bindir}
    install -m 0755 ${S}/listener.py ${D}${bindir}/infusion-pump-app

    # 2. Instala o script de init em /etc/init.d
    install -d ${D}${sysconfdir}/init.d
    install -m 0755 ${S}/infusion-pump-init ${D}${sysconfdir}/init.d/infusion-pump
}

# Herda a classe update-rc.d para registrar o boot automático
inherit update-rc.d

INITSCRIPT_NAME = "infusion-pump"
INITSCRIPT_PARAMS = "defaults"
