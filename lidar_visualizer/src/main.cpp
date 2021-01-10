#include <SFML/Graphics.hpp>
#include <iostream>
#include <sys/stat.h>
#include <unistd.h>
#include <filesystem>

void drawRadarView(sf::RenderWindow &win, sf::CircleShape &circle)
{
    circle.setFillColor(sf::Color::Black);

    // 3 externals rings
    for (int i = 6; i >= 2; i-=2) {
        circle.setRadius(i * 100);
        circle.setOrigin(i * 100, i * 100);
        circle.setOutlineThickness(i);
        win.draw(circle);
    }

    // center circle
    circle.setRadius(50);
    circle.setFillColor(sf::Color::Green);
    circle.setOrigin(50, 50);
    win.draw(circle);
}

void draw_hud(sf::RenderWindow &win, sf::Text &text)
{
    text.setCharacterSize(45);
    text.setPosition(1300, 10);
    text.setString("Keys : ");
    win.draw(text);

    int y = 100;
    text.setCharacterSize(30);
    for (auto &txt : {"s  -> Start Lidar",
                      "t  -> Stop Lidar",
                      "p  -> Toggle Freeze Screen"}) {
        text.setPosition(1300, y);
        text.setString(txt);
        win.draw(text);
        y += 50;
    }
}

int main(int argc, const char **argv)
{
    if (argc != 2) {
        std::cerr << "Usage: ./lidar_visualizer port" << std::endl;
        return EXIT_FAILURE;
    }

    if (!std::filesystem::exists(argv[1])) {
        std::cerr << "No such file: " << argv[1]  << std::endl;
        return EXIT_FAILURE;
    }

    // create window
    sf::RenderWindow win;
    win.create(sf::VideoMode(1800, 1200), "Lidar Visualizer", sf::Style::Default);
    win.setFramerateLimit(60);

    // create cirle
    sf::CircleShape circle;
    circle.setOrigin(600, 600);
    circle.setPosition(600, 600);
    circle.setFillColor(sf::Color::Black);
    circle.setOutlineColor(sf::Color::Green);

    // create line separation
    sf::RectangleShape rect;
    rect.setFillColor(sf::Color::White);
    rect.setSize(sf::Vector2f(10, 1200));
    rect.setPosition(1250, 0);

    // create text and font
    sf::Font font;
    font.loadFromFile("lemon_font.otf");
    sf::Text text;
    text.setFont(font);

    sf::Event evt;

    while (win.isOpen()) {
        while (win.pollEvent(evt)) {
            if (evt.type == sf::Event::Closed) {
                win.close();
            }
            if (evt.type == sf::Event::KeyPressed && sf::Keyboard::isKeyPressed(sf::Keyboard::Escape)) {
                win.close();
            }
        }
        win.clear(sf::Color::Black);
        drawRadarView(win, circle);
        win.draw(rect);
        draw_hud(win, text);
        win.display();
    }
    return EXIT_SUCCESS;
}