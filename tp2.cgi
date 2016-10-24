#!/usr/bin/perl -w

#Script que dibuja un formulario en html para introducir productos
#lee los 2 primeros caracteres del producto (categoria) y si coincide
#con la categoria del fichero /tmp/categorias guarda la información en
# /tmp/productos

use CGI;
$query = new CGI;

print $query->header;
print $query->start_html('Formulario Básico');

if (!$query->param) {

	print $query->start_form;
	print $query->h3('Nombre del producto');
	print $query->textfield(-name=>'name',-size=>10);
	print $query->h3('Descripcion del Producto');
	print $query->textfield(-name=>'description',-size=>10);
	print $query->h3('Precio del Producto');
	print $query->textfield(-name=>'price',-size=>3);
	print $query->br;
	print $query->br;
	print $query->submit(-value=>'Enviar');
	print $query->end_form;

} else {
	$name = $query->param('name');
	$description = $query->param('description');
	$price = $query->param('price');
	my $fileProductos = "/tmp/productos";
	# Comprobación mediante expresión regular
	if($name =~ m/^..-.+/i){   # para estar de acuerdo con el enunciado primitivo
		my $filename = '/tmp/categorias';
		#Abrimos archivo categorias
		open(my $fh, '<:encoding(UTF-8)', $filename)	
	  		or die "Could not open file '$filename' $!";	 
		while (<$fh>) {
                  chomp;
		  # Si coincide con la categoria se escribe en productos
                  if(substr($name,0,2) eq $_) {
				open F, ">> /tmp/productos" or die "Problema $!";
				print F "$name $description $price\n";  
				close F;
				return;  
			}                
		    }	 
        	}
	}
print $query->h3("NO coincide la categoria");
print $query->end_html;
