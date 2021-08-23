import os
import sys

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt


def plot_loss_accuracy(results):
    fig, axes = plt.subplots(1, 2, figsize=(10, 15))

    acc = results.history['acc']
    loss = results.history['loss']

    val_acc = results.history['val_acc']
    val_loss = results.history['val_loss']

    epochs = np.arange(1, len(acc) + 1)

    axes[0].plot(epochs, acc)
    axes[0].plot(epochs, val_acc)
    axes[0].set_title("Train and Validation Accuracies")
    axes[0].set_xlabel("Epoch")
    axes[0].set_ylabel("Accuracy")

    axes[1].plot(epochs, loss)
    axes[1].plot(epochs, val_loss)
    axes[1].set_title("Train and Validation Loss")
    axes[1].set_xlabel("Epoch")
    axes[1].set_ylabel("Binary cross-entropy loss")

    return fig
