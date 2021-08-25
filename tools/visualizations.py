import os
import sys

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt

from sklearn.metrics import confusion_matrix

ANNOT_KWS = {
    'size': 18
}


def plot_loss_accuracy(results):
    fig, axes = plt.subplots(1, 2, figsize=(15, 8))

    acc = results.history['acc']
    loss = results.history['loss']

    val_acc = results.history['val_acc']
    val_loss = results.history['val_loss']

    epochs = np.arange(1, len(acc) + 1)

    axes[0].plot(epochs, acc, label="Training Accuracy")
    axes[0].plot(epochs, val_acc, label="Validation Accuracy")
    axes[0].set_title("Train and Validation Accuracies")
    axes[0].set_xlabel("Epoch")
    axes[0].set_ylabel("Accuracy")
    axes[0].legend()

    axes[1].plot(epochs, loss, label='Training Loss')
    axes[1].plot(epochs, val_loss, label='Validation Loss')
    axes[1].set_title("Train and Validation Loss")
    axes[1].set_xlabel("Epoch")
    axes[1].set_ylabel("Binary cross-entropy loss")
    axes[1].legend()

    return fig


def plot_confusion_matrices(model, train_images, test_images, train_labels, test_labels):
    """Plot confusion matrices for train and test sets"""

    train_pred_labels = (model.predict(train_images) > 0.5).astype('int32')
    test_pred_labels = (model.predict(test_images) > 0.5).astype('int32')

    train_cm = confusion_matrix(train_labels, train_pred_labels)
    test_cm = confusion_matrix(test_labels, test_pred_labels)

    fig, axes = plt.subplots(1, 2, figsize=(18, 8))

    sns.heatmap(data=train_cm,
                cmap='Greens',
                annot=True,
                fmt='d',
                annot_kws=ANNOT_KWS,
                ax=axes[0]
                )
    axes[0].set_title('Training', fontsize=24)
    axes[0].set_xlabel('Predicted Label')
    axes[0].set_ylabel('True Label')

    sns.heatmap(data=test_cm,
                cmap='Blues',
                annot=True,
                fmt='d',
                annot_kws=ANNOT_KWS,
                ax=axes[1]
                )
    axes[1].set_title('Testing', fontsize=24)
    axes[1].set_xlabel('Predicted Label')
    axes[1].set_ylabel('True Label')

    plt.show()
