from selenium.webdriver.common.by import By


class SortablePageLocators:
    TAB_LIST = (By.CSS_SELECTOR, 'a#demo-tab-list')
    LIST_ITEM = (By.CSS_SELECTOR, 'div[id="demo-tabpane-list"] div[class="list-group-item list-group-item-action"]')
    TAB_GRID = (By.CSS_SELECTOR, 'a#demo-tab-grid')
    GRID_ITEM = (By.CSS_SELECTOR, 'div[id="demo-tabpane-grid"] div[class="list-group-item list-group-item-action"]')


class SelectablePageLocators:
    TAB_LIST = (By.CSS_SELECTOR, 'a#demo-tab-list')
    LIST_ITEM = (
        By.CSS_SELECTOR, 'ul[id= "verticalListContainer"] li[class="mt-2 list-group-item list-group-item-action"]')
    LIST_ITEM_ACTIVE = (
        By.CSS_SELECTOR,
        'ul[id= "verticalListContainer"] li[class="mt-2 list-group-item active list-group-item-action"]')
    TAB_GRID = (By.CSS_SELECTOR, 'a#demo-tab-grid')
    GRID_ITEM = (By.CSS_SELECTOR, 'div[id="gridContainer"] li[class="list-group-item list-group-item-action"]')
    GRID_ITEM_ACTIVE = (
        By.CSS_SELECTOR, 'div[id="gridContainer"] li[class="list-group-item active list-group-item-action"]')


class ResizablePageLocators:
    RESIZABLE_BOX_HANDLE = (
        By.CSS_SELECTOR, 'div[class="constraint-area"] span[class="react-resizable-handle react-resizable-handle-se"]')
    RESIZABLE_BOX = (By.CSS_SELECTOR, 'div#resizableBoxWithRestriction')
    RESIZABLE_HANDLE = (By.CSS_SELECTOR, 'div#resizable span[class="react-resizable-handle react-resizable-handle-se"]')
    RESIZABLE = (By.CSS_SELECTOR, 'div#resizable')


class DroppablePageLocators:
    # Simple
    SIMPLE_TAB = (By.CSS_SELECTOR, "a#droppableExample-tab-simple")
    DRAG_ME_SIMPLE = (By.CSS_SELECTOR, 'div#draggable')
    DROP_HERE_SIMPLE = (By.CSS_SELECTOR, '#simpleDropContainer #droppable')

    # Accept
    ACCEPT_TAB = (By.CSS_SELECTOR, "a#droppableExample-tab-accept")
    ACCEPTABLE = (By.CSS_SELECTOR, 'div#acceptable')
    NOT_ACCEPTABLE = (By.CSS_SELECTOR, 'div#notAcceptable')
    DROP_HERE_ACCEPT = (By.CSS_SELECTOR, '#acceptDropContainer #droppable')

    # Prevent Propogation
    PREVENT_TAB = (By.CSS_SELECTOR, "a#droppableExample-tab-preventPropogation")
    NOT_GREEDY_DROP_BOX_TEXT = (By.CSS_SELECTOR, "div#notGreedyDropBox p:nth-child(1)")
    NOT_GREEDY_INNER_BOX = (By.CSS_SELECTOR, "div#notGreedyInnerDropBox")
    GREEDY_DROP_BOX_TEXT = (By.CSS_SELECTOR, "div#greedyDropBox p:nth-child(1)")
    GREEDY_INNER_BOX = (By.CSS_SELECTOR, "div#greedyDropBoxInner")
    DRAG_ME_PREVENT = (By.CSS_SELECTOR, "#ppDropContainer #dragBox")

    # Revert Draggable
    REVERT_TAB = (By.CSS_SELECTOR, "a#droppableExample-tab-revertable")
    WILL_REVERT = (By.CSS_SELECTOR, "div#revertable")
    NOT_REVERT = (By.CSS_SELECTOR, "div#notRevertable")
    DROP_HERE_REVERT = (By.CSS_SELECTOR, "#revertableDropContainer #droppable")



