from abc import ABC, abstractmethod
from pdf2image import convert_from_path
import os
import ghostscript
import locale
import cv2
from PIL import Image

class Remover(ABC):
    @abstractmethod
    def remove(self, directory: str):
        pass

    @abstractmethod
    def returnImage(self, directory: str):
        pass

    def pdf2jpeg(self, PDFDirectory, JPEGDirectory):
        args = ["pef2jpeg", "-dNOPAUSE", "-sDEVICE=jpeg", "-r144", "-sOutputFile=" + JPEGDirectory, PDFDirectory]
        encoding = locale.getpreferredencoding()
        args = [a.encode(encoding) for a in args]
        ghostscript.Ghostscript(*args)

class TableRemover(Remover):
    def returnImage(self, directory: str):
        if directory.endswith(".pdf") or directory.endswith(".PDF"):
            JPEGDirectory = directory[:-4] + ".png"
            super().pdf2jpeg(directory, JPEGDirectory)
            return JPEGDirectory
            #os.remove(JPEGDirectory)
        else:
            print("zle rozszerzenie pliku prosze wybrac ponownie")
            return None

    def remove(self, directory: str):
        image = cv2.imread(directory)
        #image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        #cv2.rectangle(image, (1348, 1301), (1624, 2321), (0, 0, 0), 3)
        cv2.rectangle(image, (1301, 1348), (2321, 1624), (255, 255, 255), cv2.FILLED)
        cv2.imwrite(directory, image)
        cv2.destroyAllWindows()
        PDFDirectory = directory[:-4] + "_EDITED.pdf"
        image1 = Image.open(directory)
        image1 = image1.convert('RGB')
        image1.save(PDFDirectory)
        image1.close()
        try:
            os.remove(directory)
        except OSError as e:
            print("Failed with:", e.strerror)
            print("Error code:", e.code)

        print("done")

class HeaderRemover(Remover):
    def returnImage(self, directory: str):
        print("bede zwracal image! HeaderRemover")

    def remove(self, directory: str):
        print("bede usuwal naglowek!")