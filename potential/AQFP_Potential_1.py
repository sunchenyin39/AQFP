import matplotlib.pyplot as plt
import numpy as np


class QFP():
    def __init__(self):
        self.phi_x = 3.2
        self.phi_in = -0.1
        self.betaL = 0.8
        self.betaq = 0.4

    def potential(self, phi_p, phi_n):
        U = (self.phi_x-phi_n)*(self.phi_x-phi_n)/self.betaL + \
            (self.phi_in-phi_p)*(self.phi_in-phi_p) / \
            (self.betaL+2*self.betaq)-2*np.cos(phi_n)*np.cos(phi_p)
        return U

    def draw(self):
        phi_x = np.linspace(-2*np.pi, 2*np.pi, 100)
        phi_y = np.linspace(-2*np.pi, 2*np.pi, 100)
        phi_p, phi_n = np.meshgrid(phi_x, phi_y)
        U = self.potential(phi_p, phi_n)
        ax = plt.axes()
        ax.contour(phi_p, phi_n, U, 100, cmap='jet')
        ax.set_xlabel('phi+')
        ax.set_ylabel('phi-')
        plt.title("betaL=%.1f,betaq=%.1f,phi_in=%.1f,phi_x=%.1f"
                  % (self.betaL, self.betaq, self.phi_in, self.phi_x))
        plt.show()

    def draw_3D(self):
        phi_x = np.linspace(-2*np.pi, 2*np.pi, 500)
        phi_y = np.linspace(-2*np.pi, 2*np.pi, 500)
        phi_p, phi_n = np.meshgrid(phi_x, phi_y)
        U = self.potential(phi_p, phi_n)
        ax = plt.axes(projection='3d')
        ax.contour3D(phi_p, phi_n, U, 100, cmap='jet')
        ax.set_xlabel('phi_p')
        ax.set_ylabel('phi_n')
        plt.title("betaL=1.0,betaq=3.0,phi_x=1.2")
        ax.set_zlabel('U')
        ax.view_init(60, 35)
        plt.show()


def main():
    a = QFP()
    a.draw()
    a.draw_3D()


if __name__ == '__main__':
    main()
