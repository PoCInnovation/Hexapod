#defaults
all: debug
flash: flash_debug
clean: clean_debug


# debug config
debug:
	@pio run -e debug

flash_debug:
	@pio run -e debug --target upload

flash_and_monitor: flash_debug
	screen /dev/ttyUSB* 115200

monitor:
	screen /dev/ttyUSB* 115200

clean_debug:
	@pio run -e debug --target clean

# release config
release:
	@pio run -e release

flash_release:
	@pio run -e release --target upload

clean_release:
	@pio run -e release --target clean

# common
clean_all: clean_debug clean_release

.PHONY: all flash clean debug flash_debug clean_debug release flash_release clean_release clean_all flash_and_monitor monitor
