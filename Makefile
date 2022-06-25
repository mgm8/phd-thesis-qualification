SRC=main
VERSION=v0.0
TARGET=thesis-${VERSION}

ifndef BUILD_DIR
	BUILD_DIR=build
endif

all:
	mkdir -p $(BUILD_DIR)
	latexmk -pdf -jobname=$(BUILD_DIR)/$(TARGET) $(SRC).tex

index:
	makeindex $(BUILD_DIR)/$(TARGET).nlo -s nomencl.ist -o $(BUILD_DIR)/$(TARGET).nls

loop:
	latexmk -pvc -pdf -halt-on-error -jobname=$(BUILD_DIR)/$(TARGET) $(SRC).tex

view:
	evince $(BUILD_DIR)/$(TARGET).pdf &

clean:
	rm -f $(BUILD_DIR)/* figures/*.eps sections/*.aux references/*.aux
