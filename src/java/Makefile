JAVAC = javac

JAVA = java


SRC = $(shell find . -name "*.java")

CLASSES = $(SRC:.java=.class)


MAIN = Deck


all: $(CLASSES)


%.class: %.java
	$(JAVAC) $<

run: all
	$(JAVA) $(MAIN)

# Clean class files
clean:
	find . -name "*.class" -delete
