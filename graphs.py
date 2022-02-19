import matplotlib.pyplot as plt
from numpy import true_divide

def GraficaPie(productos, ventas, fullpathgraficas):
    labels = productos
    sizes = ventas

    fig,ax1 = plt.subplots()
    ax1.pie(sizes, explode=None, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.savefig(fullpathgraficas, bbox_inches='tight')
    plt.show()

    return

def GraficaBarras(productos, ventas, fullpathgraficas):
    fig, ax = plt.subplots(figsize=(12, 5.4))
    ax.bar(productos, ventas)

    plt.savefig(fullpathgraficas, bbox_inches='tight')
    plt.show()

def GraficaLineas(productos, ventas, fullpathgraficas):
    fig, ax = plt.subplots(figsize=(12, 5.4))
    #ax[0,0].set_title(titulografica)
    ax.plot(productos, ventas)

    plt.savefig(fullpathgraficas, bbox_inches='tight')
    plt.show()