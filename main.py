from containers.menu.menu import Menu
from core.program import Program


def main():
    program = Program()
    program.window.set_size(1280, 720)
    program.window.set_background((245, 245, 245))
    
    program.set_container(Menu)
    
    program.run()

if __name__ == '__main__':
    main()
