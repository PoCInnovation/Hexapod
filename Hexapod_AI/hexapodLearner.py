#!/usr/bin/python3
import tensorflow as tf

def main():

    # TODO INITIALISE HEXAPOD

    init = tf.global_variables_initializer()
    saver = tf.train.Saver()

    with tf.Session() as sess:
        sess.run(init)

        # TODO ML

if __name__== "__main__":
    main()