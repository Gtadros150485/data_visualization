import matplotlib.pyplot as plt


def draw(xs,ys):
    fig, ax = plt.subplots()
    plt.style.use("bmh")
    ax.scatter(xs,ys, linewidth = 3, color= "blue")
    ax.axis([0,100, 5, 1000])
    ax.set_title("This is a graph", fontsize = 24, color= "orange")
    ax.set_xlabel("x-axis", fontsize = 14, color="brown" )
    ax.set_ylabel("y-axis", fontsize = 14, color="red")

    plt.show()


ys = [1, 4, 9, 16, 25]
xs = [1,2,3,4,5]

plt.show()
draw(xs, ys)






