#include "Gui.hpp"

Gui::Gui(std::string &port) : _port(port)
{
    // create window
    _win.create(sf::VideoMode(1800, 1200), "Lidar Visualizer", sf::Style::Default);
    _win.setFramerateLimit(60);

    // create cirle
    _circle.setOrigin(600, 600);
    _circle.setPosition(600, 600);
    _circle.setFillColor(sf::Color::Black);
    _circle.setOutlineColor(sf::Color::Green);

    // create line separation
    _rect.setFillColor(sf::Color::White);
    _rect.setSize(sf::Vector2f(10, 1200));
    _rect.setPosition(1250, 0);

    // create text and font
    _font.loadFromFile("lemon_font.otf");
    _text.setFont(_font);
}

void Gui::drawRadarView()
{
    _circle.setFillColor(sf::Color::Black);

    // 3 externals rings
    for (int i = 6; i >= 2; i-=2) {
        _circle.setRadius(i * 100);
        _circle.setOrigin(i * 100, i * 100);
        _circle.setOutlineThickness(i);
        _win.draw(_circle);
    }

    // center _circle
    _circle.setRadius(50);
    _circle.setFillColor(sf::Color::Green);
    _circle.setOrigin(50, 50);
    _win.draw(_circle);
}

void Gui::drawHUD()
{
    _text.setCharacterSize(45);
    _text.setPosition(1300, 10);
    _text.setString("Keys : ");
    _win.draw(_text);

    int y = 100;
    _text.setCharacterSize(30);
    for (auto &txt : {"s  -> Start Lidar",
                      "t  -> Stop Lidar",
                      "p  -> Toggle Freeze Screen"}) {
        _text.setPosition(1300, y);
        _text.setString(txt);
        _win.draw(_text);
        y += 50;
    }
    _text.setPosition(1270, 1160);
    _text.setString(_port);
    _win.draw(_text);

}

void Gui::start()
{
    sf::Event evt;

    while (_win.isOpen()) {
        while (_win.pollEvent(evt)) {
            if (evt.type == sf::Event::Closed) {
                _win.close();
            }
            if (evt.type == sf::Event::KeyPressed && sf::Keyboard::isKeyPressed(sf::Keyboard::Escape)) {
                _win.close();
            }
        }
        _win.clear(sf::Color::Black);
        this->drawRadarView();
        _win.draw(_rect);
        this->drawHUD();
        _win.display();
    }
}