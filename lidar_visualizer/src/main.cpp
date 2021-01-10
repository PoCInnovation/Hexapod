#include <SFML/Graphics.hpp>

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

int main(int argc, const char **argv)
{
    // create window
    sf::RenderWindow win;
    win.create(sf::VideoMode(1200, 1200), "Lidar Visualizer", sf::Style::Default);
    win.setFramerateLimit(60);

    // create cirle
    sf::CircleShape circle;
    circle.setOrigin(600, 600);
    circle.setPosition(600, 600);
    circle.setFillColor(sf::Color::Black);
    circle.setOutlineColor(sf::Color::Green);

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
        win.display();
    }
    return 0;
}
