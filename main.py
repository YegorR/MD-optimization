from marquardt import marquardt
import tkinter as tk
import tkinter.messagebox as tk_mb

class Window:
    def __init__(self):
        self.root = None
        self.f_entry = None
        self.f_label = None
        self.x_entry = None
        self.x_label = None
        self.eps_entry = None
        self.eps_label = None

        self.decision_x_label = None
        self.decision_x_entry = None
        self.decision_y_label = None
        self.decision_y_entry = None

        self.f_var = None
        self.x_var = None
        self.eps_var = None
        self.decision_x_var = None
        self.decision_y_var = None

        self.calc_button = None

        self.TEXT_WIDTH = 100
        self.PAD_X = 2
        self.PAD_Y = 5
        self.WIDTH = 800
        self.HEIGHT = 200


    def start(self):
        self.root = tk.Tk()
        self.root.title("YegorR: Оптимизация многомерной функции")
        self.root.geometry(str(self.WIDTH)+"x"+str(self.HEIGHT))
        self.root.resizable(width=False, height=False)
        self.init_vars()
        self.widgets()
        self.layout()

        self.loop()

    def loop(self):
        self.root.mainloop()

    def init_vars(self):
        self.f_var = tk.StringVar(value="1000*((x[1]-(x[0]**2))**2)+((1-x[0])**2)")
        self.x_var = tk.StringVar(value="10, -55")
        self.eps_var = tk.StringVar(value="0.001")
        self.decision_x_var = tk.StringVar()
        self.decision_y_var = tk.StringVar()


    def widgets(self):
        self.f_entry = tk.Entry(self.root, width=self.TEXT_WIDTH,
                                textvariable=self.f_var)
        self.f_label = tk.Label(self.root, text="f")
        self.x_entry = tk.Entry(self.root, width=self.TEXT_WIDTH,
                                textvariable=self.x_var)
        self.x_label = tk.Label(self.root, text="x0")
        self.eps_entry = tk.Entry(self.root, width=self.TEXT_WIDTH,
                                  textvariable=self.eps_var)
        self.eps_label = tk.Label(self.root, text="Точность")
        self.decision_x_entry = tk.Entry(self.root, width=self.TEXT_WIDTH,
                                         textvariable=self.decision_x_var)
        self.decision_x_label = tk.Label(self.root, text="Точка минимума")
        self.decision_y_entry = tk.Entry(self.root, width=self.TEXT_WIDTH,
                                         textvariable=self.decision_y_var)
        self.decision_y_label = tk.Label(self.root, text="Значение минимума")

        self.calc_button = tk.Button(self.root, text="Решение",
                                     command=self.calculate)


    def layout(self):
        self.f_label.grid(row=0, column=0, padx=self.PAD_X, pady=self.PAD_Y,
                          sticky=tk.W)
        self.f_entry.grid(row=0, column=1, padx=self.PAD_Y, pady=self.PAD_Y,
                          sticky=tk.W)
        self.x_label.grid(row=1, column=0, padx=self.PAD_X, pady=self.PAD_Y,
                          sticky=tk.W)
        self.x_entry.grid(row=1, column=1, padx=self.PAD_Y, pady=self.PAD_Y,
                          sticky=tk.W)
        self.eps_label.grid(row=2, column=0, padx=self.PAD_Y, pady=self.PAD_Y,
                            sticky=tk.W)
        self.eps_entry.grid(row=2, column=1, padx=self.PAD_Y, pady=self.PAD_Y,
                            sticky=tk.W)
        self.calc_button.grid(row=3, column=0, columnspan=2, pady=self.PAD_Y)
        self.decision_x_label.grid(row=4, column=0, padx=self.PAD_Y,
                                   pady=self.PAD_Y, sticky=tk.W)
        self.decision_x_entry.grid(row=4, column=1, padx=self.PAD_Y,
                                   pady=self.PAD_Y, sticky=tk.W)
        self.decision_y_label.grid(row=5, column=0, padx=self.PAD_Y,
                                   pady=self.PAD_Y, sticky=tk.W)
        self.decision_y_entry.grid(row=5, column=1, padx=self.PAD_Y,
                                   pady=self.PAD_Y, sticky=tk.W)

    def calculate(self):
        if not self.validate_date():
            return
        x_0 = self.parsing(self.x_var.get())
        for i in range(len(x_0)):
            x_0[i] = float(x_0[i])
        eps = float(self.eps_var.get())

        try:
            f = lambda x: eval(self.f_var.get())
            x_min, f_min = marquardt(x_0, 500, eps, f)
        except OverflowError:
            tk_mb.showwarning("Ошибка", "Ошибка переполнения")
            return
        self.decision_x_var.set(str(x_min))
        self.decision_y_var.set(str(f_min))


    def validate_date(self):
        try:
            x = self.parsing(self.x_var.get())
            for i in range(len(x)):
                x[i] = float(x[i])
        except ValueError:
            tk_mb.showwarning("Ошибка", "Введите корректный x0")
            return False
        try:
            eps = float(self.eps_var.get())
        except ValueError:
            tk_mb.showwarning("Ошибка", "Введите корректную точность")
            return False
        try:
            float(eval(self.f_var.get()))
        except SyntaxError:
            tk_mb.showwarning("Ошибка", "Введите корректную функцию")
            return False
        except IndexError:
            tk_mb.showwarning("Ошибка", "Введите корректную функцию")
            return False
        except ValueError:
            tk_mb.showwarning("Ошибка", "Введите корректную функцию")
            return False
        return True

    @staticmethod
    def parsing(x):
        li = x.split(',')
        for i in range(len(li)):
            li[i] = li[i].strip()
        return li


if __name__ == "__main__":
    window = Window()
    window.start()
