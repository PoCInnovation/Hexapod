#ifndef BLE_CON_HPP
#define BLE_CON_HPP

#include <functional>

namespace BleCon {
    void init();
    void updateEvents();
    void setCallback(std::function<void(std::string str)> func);
}  // namespace BleCon

#endif /* BLE_CON_HPP */
