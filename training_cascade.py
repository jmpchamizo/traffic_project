import matplotlib
import pickle



def create_training_files(name="stop"):
    # Costruuye los directorios que contendrán las imagenes y los archivos de texto que se usan para entrenar
    # un Image Classifier.
    pos, neg = get_pos_array_of_sign(name)
    create_file("pos", name, pos)
    create_file(array_images= neg)



def create_file(typ="neg", traffic_sign_name="neg", array_images=[]):
    # · Creará un directorio en data/training/<name_image>/<typ> que contendrá las imágenes del array que pasemos
    #    Estas las nombrará como <traffic_sign_name>.jpg para las imagenes positivas y neg.jpg para las negativas
    # · Creará en el directorio raiz un archivo con nombre <traffic_sign_name>.info para el caso en el 
    #   queramos crear el archivo de imagenes positivas y bt.txt cuando queramos crear el de imagenes negativas
    name = "bt.txt" if typ == "neg" else f'{traffic_sign_name}.info'
    name_image = typ if typ == "neg" else traffic_sign_name
    f= open(name,"w+")
    for i,arr in enumerate(array_images):
        matplotlib.image.imsave(f'data/training/{name_image}/{typ}/{name_image}{i}.jpg', arr[0,:,:])   
        f.write(f"data/training/{name_image}/{typ}/{name_image}{i}.jpg 1 0 0 32 32\n" )
    f.close()



def get_pos_array_of_sign(name="stop"):
    # Devuelve una tupla de arrays en la que el primer array es un numpy array con las imagenes de la señal
    # de nombre name y el segundo, otro numpy array con el mismo número de imagenes pero de otras señales 
    # ambas en escala de grises.
    mfile = open('data/data8.pickle','rb')
    new_dict = pickle.load(mfile)
    return (new_dict["x_train"][new_dict['y_train']==14], new_dict["x_train"][new_dict['y_train']!=14])
