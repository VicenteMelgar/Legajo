modalidad = (
  ('CAS', 'CAS'),
  ('Nombrado', 'Nombrado'),
  ('Cesante', 'Cesante')
)

documentos_regimen = (
  ('276', 'Régimen 276'),
  ('CAS', 'Contrato Administrativo de Servicios'),
  ('30057', 'Régimen de Servicio Civil' )
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
  (10, 'Nombramiento'),
  (20, 'Contrato Administrativo de Servicios'),
  (30, 'Contrato a plazo fijo'),
  (40, 'Destaque de otra Dependencia'),
  (50, 'Designación de otra Dependencia'),
)

tipo_desplazamiento = (
  (10, 'Designación'),
  (20, 'Rotación'),
  (30, 'Destaque'),
  (40, 'Encargatura')
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
  (10, 'Resolución Administrativa'),
  (20, 'Resolución Directoral'),
  (30, 'Memorando')
)

documentos_informacion = [
  ("Ficha de datos", "Ficha de datos"),
  ("Documento Nacional de Identidad – DNI", "Documento Nacional de Identidad – DNI"),
  ("Declaración jurada o Certificado de antecedentes penales", "Declaración jurada o Certificado de antecedentes penales"),
  ("Declaración jurada o certificado de antecedentes policiales", "Declaración jurada o certificado de antecedentes policiales"),
  ("Declaración Jurada de bienes y rentas", "Declaración Jurada de bienes y rentas"),
  ("Declaración Jurada de no tener impedimentos (Ley N° 31419)", "Declaración Jurada de no tener impedimentos (Ley N° 31419)"),
  ("Partida de matrimonio o constancia de concubinato", "Partida de matrimonio o constancia de concubinato"),
  ("Información de impedimentos e inhabilitaciones", "Información de impedimentos e inhabilitaciones"),
  ("DNI de el/la cónyuge o concubino/a", "DNI de el/la cónyuge o concubino/a"),
  ("DNI de los/las hijos/as menores de edad", "DNI de los/las hijos/as menores de edad"),
  ("Certificado de discapacidad de el/la servidor/a", "Certificado de discapacidad de el/la servidor/a"),
  ("Certificado de discapacidad de los/las hijos/as", "Certificado de discapacidad de los/las hijos/as"),
  ("Declaración Jurada por Nepotismo", "Declaración Jurada por Nepotismo"),
  ("Otro Documento", "Otro Documento"),
]

documentos_seleccion = [
  ("Resultado Final de proceso de selección", "Resultado Final de proceso de selección"),
  ("Informe de la Oficina de Personal", "Informe de la Oficina de Personal"),
  ("Otro Documento", "Otro Documento"),
]

documentos_induccion = [
  (10, "Registro de Inducción"),
  (20, "Cargo de entrega de perfil de puesto y funciones"),
  (30, "Cargo de entrega de reglamento interno de servidores civiles"),
  (40, "Cargo de entrega de código de conducta y ética"),
]

documentos_prueba = [
  (10, "Evaluación y resultados del período de prueba"),
]

documentos_colegiatura = [
  (10, "Colegiatura"),
  (20, "Habilitación Profesional"),
  (30, "SERUM"),
]

documentos_grado = [
  (10, "Secundaria Completa"),
  (20, "Superior Técnica Incompleta"),
  (30, "Superior Técnica"),
  (40, "Superior Universitario Incompleta"),
  (50, "Superior Universitario"),
  (60, "Especialidad"),
  (70, "Maestría"),
  (80, "Doctorado"),
]

documentos_especialidad = [
  (10, "Especialidad"),
  (20, "Subespecialidad"),
]


documentos_cursos = [
  (10, "Especialización"),
  (20, "Diplomado"),
  (30, "Congreso"),
  (40, "Convención"),
  (50, "Conferencia"),
  (60, "Curso de capacitación"),
  (70, "Seminario"),
  (80, "Simposio"),
  (90, "Charla"),
  (100, "Taller"),
  (110, "Certificado"),
  (120, "Constancia"),
]

documentos_experiencia = [
  (10, "Certificado"),
  (20, "Constancia"),
  (30, "Resolución"),
  (40, "Memorando"),
]

documentos_retencion = [
  (10, "Exoneración de retención de cuarta categoría"),
  (20, "Exoneración de retención de quinta categoría"),
]

documentos_evaluacion = [
  (10, "Factores de evaluación"),
  (20, "Registro de evidencias"),
  (30, "Formato de reunión de seguimiento"),
  (40, "Notificación de evaluación obtenida"),
  (50, "Acta de retroalimentación de resultados de desempeño"),
  (60, "Plan de mejora"),
]

documentos_reconocimientos = [
  (10, "Reconocimiento"),
  (20, "Sanción"),
]

documentos_laboral = [
  (10, "Controversias Individuales"),
  (20, "Controversias Colectivas"),
  (30, "Afiliación al Sindicato"),
]

documentos_sst = [
  (10, "Cargo de entrega del Reglamento de SST"),
  (20, "Registro de entrenamiento, y simulacros de emergencias"),
  (30, "Capacitaciones brindadas por la entidad"),
  (40, "Trámites y gestiones de seguro"),
  (50, "Trámites y gestiones de subsidios"),
  (60, "Descanso Médico"),
  (70, "Afiliaciones a Entidades Prestadoras de Salud (EPS)"),
  (80, "Otro Documento"),
]

documentos_desvinculacion = [
  (10, "Informe de Gestión"),
  (20, "Entrega de cargo/puesto"),
  (30, "Liquidación de beneficios sociales y/o pensión"),
  (40, "Carta de no renovación de contrato a plazo determinado"),
  (50, "Otro Documento"),
]

motivo_progresion = [
  (10, "Ascenso"),
  (20, "Cambio de grupo Ocupacional"),
]

tipo_movimientos = [
  (10, "LSGH"),
  (20, "LCGH"),
]