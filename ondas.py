import matplotlib.pyplot as plt
from mpl_toolkits.axisartist.axislines import SubplotZero
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# X, Y, Z, U, V, W = zip(*soa)

def plot_polarized_light(intensities, deltaPhase=0, fig=None, show_components=False):
    if fig is None:
        fig = plt.figure(figsize=(20,10))

    X = np.linspace(0, 2*np.pi)
    Y = np.zeros_like(X)
    Z = np.zeros_like(X)

    V = intensities[0]*np.sin(X)
    W = intensities[1]*np.sin(X-deltaPhase)
    U = np.zeros_like(W)
    ax = fig.add_subplot(121, projection='3d', azim=-25, elev=20)

    ax.quiver(X, Y, Z, U, V, W, arrow_length_ratio=0.05, label="E")

    if show_components:
        ax.quiver(X, Y, Z, U, V, np.zeros_like(W), color=(1,0,0,1), arrow_length_ratio=0.05, label="Ex")
        ax.quiver(X, Y, Z, U, np.zeros_like(V), W, color=(0,1,0,1), arrow_length_ratio=0.05, label="Ey")

    ax.legend()


    X_ax = np.array([-(1), 0, 0])
    Y_ax = np.array([0, 1, 0])
    Z_ax = np.array([0, 0, -1])
    U_ax = np.array([5+2*np.pi, 0, 0])
    V_ax = np.array([0, -1.5, 0])
    W_ax = np.array([0, 0, 1.5])
    ax.quiver(X_ax, Y_ax, Z_ax, U_ax, V_ax, W_ax, arrow_length_ratio=0.01,color=(0,0,0,1))

    for x,y,z, txt in zip(X_ax+U_ax, Y_ax+V_ax, Z_ax+W_ax, ["Z","X","Y"]):
        ax.text(x-0.1,y,z,txt, fontsize=16)

    ax_2d = SubplotZero(fig, 122)
    fig.add_subplot(ax_2d)


    theta = np.linspace(0, 2*np.pi, 1000)
    ax_2d.plot(np.cos(theta),np.sin(theta),'k--', linewidth=2)

    # plt.annotate(s='Ey', xy=(0, -intensities[1]), xytext=(0, intensities[1]), horizontalalignment='center',
    #              verticalalignment='center',
    #              color='black', arrowprops=dict(arrowstyle='<->'),fontsize=18)
    #              verticalalignment='center',
    #              color='black', arrowprops=dict(arrowstyle='<->', shrinkA=0, shrinkB=0), 
    ax_2d.plot(V,W,'b-', linewidth=5)

    if intensities[0]>1e-4:
        ax_2d.arrow(-0.8*intensities[0], 0, 1.8*intensities[0],0, linewidth=0, width=0.01, color='black',shape="full", length_includes_head=True)
        ax_2d.arrow(+0.8*intensities[0], 0, -1.8*intensities[0],0, linewidth=0, width=0.01, color='black',shape="full", length_includes_head=True)
        plt.annotate(s='Ex', xy=(-0.9*intensities[0],0.03), xytext=(0.9*intensities[0],0.02),horizontalalignment='center',fontsize=18, color='black')

    if intensities[1]>1e-4:
        ax_2d.arrow(0, -0.8*intensities[1],  0, 1.8*intensities[1], linewidth=0, width=0.01, color='black', shape="full", length_includes_head=True)
        ax_2d.arrow(0, +0.8*intensities[1], 0, -1.8*intensities[1], linewidth=0, width=0.01, color='black',shape="full", length_includes_head=True)
        plt.annotate(s='Ey', xy=(0.06,-0.9*intensities[1]), xytext=(0.06,0.9*intensities[1]),horizontalalignment='center',fontsize=18, color='black')
    # ax_2d.plot([0, 0],[0,intensities[1]],'k->', linewidth=4)

    ax_2d.set_xlim([-1.1,1.1])
    ax_2d.set_ylim([-1.1,1.1])
    # # ax_2d.text(1,0,"X", fontsize=16)
    # # ax_2d.text(0,1,"Y", fontsize=16)
    plt.xticks([])
    plt.yticks([])
    ax_2d.axis('off')
    # for direction in ["xzero", "yzero"]:
    #     ax_2d.axis[direction].set_axisline_style("-|>")
    #     ax_2d.axis[direction].set_visible(True)
    for direction in ["left", "right", "bottom", "top"]:
        ax_2d.axis[direction].set_visible(False)


    ax.set_axis_off()

    ax.set_xlim([0, 2*np.pi])
    ax.set_ylim([-0.4, 0.4])
    ax.set_zlim([-0.4, 0.4])
    fig.tight_layout()
    plt.show()


alpha=1*np.pi/6
intensities = np.array((np.cos(alpha), np.sin(alpha)))
intensities /= np.linalg.norm(intensities)
plot_polarized_light(intensities=intensities, deltaPhase=0, fig=None, show_components=True)

# plot_polarized_light(intensities=(1,1), deltaPhase=np.pi/3, fig=None, show_components=True)
