# Diz ao bitbake para procurar arquivos nesta pasta 'files' primeiro
FILESEXTRAPATHS:prepend := "${THISDIR}/files:"

# Adiciona o nosso arquivo de configuração à lista de fontes
SRC_URI:append = " file://wpa_supplicant.conf-sane"

# Garante que o arquivo seja instalado no lugar certo com as permissões certas
do_install:append () {
    install -d ${D}${sysconfdir}/wpa_supplicant/
    install -m 600 ${WORKDIR}/wpa_supplicant.conf-sane ${D}${sysconfdir}/wpa_supplicant.conf
}

