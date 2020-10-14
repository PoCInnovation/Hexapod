#ifndef HEXAPODACTIONS_HPP
#define HEXAPODACTIONS_HPP

class HexapodActions{
    public:
        HexapodActions();
        ~HexapodActions() = default;
        void forward();
        void backward();
        void stop();
        void stand();
        void turnRight();
        void turnLeft();

    private:
};

#endif // HEXAPODACTIONS_HPP
