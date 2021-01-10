#ifndef GUI_HPP
#define GUI_HPP

#include <SFML/Graphics.hpp>
#include <string.h>

class Gui
{
private:
    sf::RenderWindow _win;
    sf::CircleShape _circle;
    sf::RectangleShape _rect;
    sf::Font _font;
    sf::Text _text;

    std::string &_port;

    void drawRadarView();
    void drawHUD();

public:
    Gui(std::string &port);
    void start();
};

#endif /* GUI_HPP */
