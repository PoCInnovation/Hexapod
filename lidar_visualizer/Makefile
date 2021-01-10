CXX = g++

NAME = lidar_visualizer

SRC_MAIN = src/main.cpp

SRC_OTHERS = src/Gui.cpp

SRC = $(SRC_OTHERS)

OBJ = $(SRC:.cpp=.o) $(SRC_MAIN:.cpp=.o)

CPPFLAGS = -std=c++17

CXXFLAGS = -Wall -Wextra -O3

LDFLAGS =

LDLIBS = -lsfml-system -lsfml-graphics -lsfml-window -lsfml-audio

all: $(NAME)

$(NAME): $(OBJ)
	$(CXX) -o $(NAME) $(OBJ) $(LDFLAGS) $(LDLIBS)

debug: CXXFLAGS += -g3 -D DEBUG
debug: fclean $(NAME)

clean:
	$(RM) $(NAME)

fclean: clean
	$(RM) $(OBJ)

re: fclean all

.PHONY: all clean fclean re debug
