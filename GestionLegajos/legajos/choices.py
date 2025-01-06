modalidad = (
  ('CAS', 'CAS'),
  ('Nombrado', 'Nombrado'),
  ('Cesante', 'Cesante')
)
estados = (
  ('S', 'Soltero/a'),
  ('C', 'Casado/a')
)

sexo = (
  ('F', 'Femenino'),
  ('M', 'Masculino')
)

tipo = (
  ('Nombramiento', 'Nombramiento'),
  ('Reasignacion', 'Reasignación'),
  ('Ascenso', 'Ascenso'),
  ('Cese', 'Cese')
)

departamento = (
  ('Amazonas', 'Amazonas'),
  ('Ancash', 'Ancash'),
  ('Apurimac', 'Apurimac'),
  ('Arequipa', 'Arequipa'),
  ('Ayacucho', 'Ayacucho'),
  ('Cajamarca', 'Cajamarca'),
  ('Callao', 'Callao'),
  ('Cusco', 'Cusco'),
  ('Huancavelica', 'Huancavelica'),
  ('Huanuco', 'Huanuco'),
  ('Ica', 'Ica'),
  ('Junin', 'Junín'),
  ('La Libertad', 'La Libertad'), 
  ('Lambayeque', 'Lambayeque'),
  ('Lima', 'Lima'),
  ('Loreto', 'Loreto'),
  ('Madre de Dios', 'Madre de Dios'),
  ('Moquegua', 'Moquegua'),
  ('Pasco', 'Pasco'),
  ('Piura', 'Piura'),
  ('Puno', 'Puno'),
  ('San Martin', 'San Martín'),
  ('Tacna', 'Tacna'),
  ('Tumbes', 'Tumbes'),
  ('Ucayali', 'Ucayali')
)

dependencia = (
  ('HHV', 'Hospital Hermilio Valdizán'),
)

cargo = (
  ('Auxiliar Administrativo', 'Auxiliar Administrativo'),
  ('Asistente Administrativo', 'Asistente Administrativo'),
  ('Coordinador', 'Coordinador')
)

nivel = (
  ('STD', 'STD'),
  ('SAA', 'SAA')
)

documento = (
  ('RA', 'Resolución Administrativa'),
  ('RD', 'Resolución Directoral'),
  ('Memo', 'Memorando')
)

documentos_informacion = [
  (3, "Ficha de datos"),
  (6, "Documento Nacional de Identidad – DNI"),
  (9, "Declaración jurada o Certificado de antecedentes penales"),
  (12, "Declaración jurada o certificado de antecedentes policiales"),
  (15, "Declaración Jurada de bienes y rentas"),
  (18, "Declaración Jurada de no tener impedimentos (Ley N° 31419)"),
  (21, "Partida de matrimonio o constancia de concubinato"),
  (24, "Información de impedimentos e inhabilitaciones"),
  (27, "DNI de el/la cónyuge o concubino/a"),
  (30, "DNI de los/las hijos/as menores de edad"),
  (33, "Certificado de discapacidad de el/la servidor/a"),
  (36, "Certificado de discapacidad de los/las hijos/as"),
]

documentos_seleccion = [
  (3, "Resultado Final de proceso de selección"),
  (6, "Informe de la Oficina de Personal"),
]

documentos_induccion = [
  (3, "Registro de Inducción"),
  (6, "Cargo de entrega de perfil de puesto y funciones"),
  (9, "Cargo de entrega de reglamento interno de servidores civiles"),
  (12, "Cargo de entrega de código de conducta y ética"),
]
