import matplotlib.pyplot as plt
import numpy as np


class QFP():
    def __init__(self):
        self.phi_0 = 2.07E-15
        self.Ic1 = 50e-6
        self.Ic2 = 50e-6
        self.L1 = 1.42e-12
        self.L2 = 1.42e-12
        self.Lq = 8.27e-12
        self.Lx = 5.19e-12
        self.Iin = -20e-6
        self.Ix = 1e-3
        self.Lin = 1.22e-12
        self.k1 = -0.22
        self.k2 = -0.22
        self.Ej = self.phi_0*self.Ic1/2/np.pi

    def potential(self, phi_1, phi_2):
        Uix = 0.5*self.Lx*self.Ix**2+0.5*self.Lin*self.Iin**2
        # Uj = -2*self.Ej*np.cos(phi_p)*np.cos(phi_n)
        # U12 = 0.5*self.L1*(1-np.cos(2*phi_p)*np.cos(2*phi_n))*self.Ic1**2
        # Um = self.k1*np.sqrt(self.L1*self.Lx)*self.Ic1 * \
        #     self.Ix*(-2*np.sin(phi_n)*np.cos(phi_p))
        # Uq = 0.5*self.Lq*(self.Iin-self.Ic1*(2*np.sin(phi_p)*np.cos(phi_n)))**2
        Uj = -self.Ej*(np.cos(phi_1)+np.cos(phi_2))
        U12=0.5*self.L1*((self.Ic1*np.sin(phi_1))**2+(self.Ic1*np.sin(phi_2))**2)
        Um=self.k1*np.sqrt(self.L1*self.Lx)*self.Ic1*self.Ix*(np.sin(phi_2)-np.sin(phi_1))
        Uq = 0.5*self.Lq*(self.Iin-self.Ic1*(np.sin(phi_1)+np.sin(phi_2)))**2
        U = Uix+Uj+U12+Um+Uq
        return U

    def draw(self):
        phi_x = np.linspace(-2*np.pi, 2*np.pi, 100)
        phi_y = np.linspace(-2*np.pi, 2*np.pi, 100)
        phi_p, phi_n = np.meshgrid(phi_x, phi_y)
        U = self.potential(phi_p, phi_n)
        fig = plt.figure()
        ax = plt.axes(projection='3d')
        ax.contour3D(phi_p, phi_n, U, 100, cmap='jet')
        ax.set_xlabel('phi_p')
        ax.set_ylabel('phi_n')
        ax.set_zlabel('U')
        ax.view_init(60, 35)
        plt.show()


def main():
    a = QFP()
    a.draw()


if __name__ == '__main__':
    main()
