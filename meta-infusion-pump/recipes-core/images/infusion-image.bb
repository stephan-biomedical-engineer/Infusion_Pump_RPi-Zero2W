SUMMARY = "Imagem Oficial da Bomba de Infusão"
LICENSE = "MIT"

# Baseia na core-image-minimal (ou core-image-base para ter mais recursos)
require recipes-core/images/core-image-minimal.bb

# Lista de pacotes que SEMPRE devem estar nesta imagem
IMAGE_INSTALL:append = " \
    linux-firmware-rpidistro-bcm43436 \
    linux-firmware-rpidistro-bcm43430 \
    kernel-module-brcmfmac \
    wpa-supplicant \
    iw \
    python3 \
    python3-pip \
    rpi-gpio \
    mosquitto \
    mosquitto-clients \
    python3-paho-mqtt \
    infusion-control \
"

