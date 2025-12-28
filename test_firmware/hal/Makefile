# ===============================
# Projeto
# ===============================
LIB_NAME := libhal.a
BUILD_DIR := build
OBJ_DIR := $(BUILD_DIR)/obj

# ===============================
# Toolchain (Yocto SDK)
# ===============================
CXX ?= g++
AR  ?= ar

CXXFLAGS := -Wall -O2 -std=c++17
CXXFLAGS += -Iinclude -Ipwm -Igpio -Ii2c

# ===============================
# Fontes
# ===============================
HAL_SRCS := \
	gpio/hal_gpio.cpp \
	pwm/hal_pwm.cpp

APP_SRCS := \
	app/motor_pwm.cpp \
	app/encoder_position.cpp

SRCS := $(HAL_SRCS) $(APP_SRCS)

OBJS := $(SRCS:%.cpp=$(OBJ_DIR)/%.o)

# ===============================
# Regras
# ===============================
all: $(LIB_NAME)

$(LIB_NAME): $(OBJS)
	$(AR) rcs $@ $^

$(OBJ_DIR)/%.o: %.cpp
	@mkdir -p $(dir $@)
	$(CXX) $(CXXFLAGS) -c $< -o $@

clean:
	rm -rf $(BUILD_DIR) $(LIB_NAME)

.PHONY: all clean
