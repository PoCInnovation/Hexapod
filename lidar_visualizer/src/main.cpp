#include <iostream>
#include <sys/stat.h>
#include <unistd.h>
#include <filesystem>
#include "Gui.hpp"
#include <string>

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
    std::string port(argv[1]);
    Gui g(port);
    g.start();
    return EXIT_SUCCESS;
}