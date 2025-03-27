condicion_laboral = (
  ('Nombrado', 'Nombrado'),
  ('Contratado', 'Contratado a Plazo Fijo'),
  ('CAS', 'Contrato Administrativo de Servicios'),
)

documento_identidad = (
  ('DNI', 'Documento Nacional de Identidad'),
  ('Carnet de Extranjería', 'Carnet de Extranjería'),
)

documentos_regimen = (
  ('276', 'Régimen del Decreto Legislativo 276'),
  ('CAS', 'Contrato Administrativo de Servicios'),
  ('30057', 'Régimen de Servicio Civil' )
)

departamento_oficina = (
  ('Oficina de Economía', 'Oficina de Economía'),
  ('Oficina de Logística', 'Oficina de Logística'),
  ('Oficina de Personal', 'Oficina de Personal'),
)

grupo_ocupacional = (
  ('Auxiliares', 'Auxiliares'),
  ('Funcionarios y Directivos', 'Funcionarios y Directivos'),
  ('Profesionales', 'Profesionales'),
  ('Profesionales de la Salud', 'Profesionales de la Salud'),
  ('Tecnicos', 'Tecnicos'),
)

tipo_historial = (
  ('Incorporación', 'Incorporación'),
  ('Progresión', 'Progresión'),
  ('Desplazamiento', 'Desplazamiento'),
  ('Desvinculación', 'Desvinculación'),
)

cargos = (
  ('ASISTENTE EJECUTIVO II', 'ASISTENTE EJECUTIVO II'),
  ('ASISTENTE EN SERVICIOS DE SALUD I', 'ASISTENTE EN SERVICIOS DE SALUD I'),
  ('ASISTENTE PROFESIONAL I', 'ASISTENTE PROFESIONAL I'),
  ('ASISTENTE/A ADMINISTRATIVO/A I', 'ASISTENTE/A ADMINISTRATIVO/A I'),
  ('AUXILIAR ADMINISTRATIVO/A', 'AUXILIAR ADMINISTRATIVO/A'),
  ('AUXILIAR ASISTENCIAL', 'AUXILIAR ASISTENCIAL'),
  ('DIRECTOR ADJUNTO', 'DIRECTOR ADJUNTO'),
  ('DIRECTOR DE HOSPITAL III', 'DIRECTOR DE HOSPITAL III'),
  ('DIRECTOR/A EJECUTIVO/A', 'DIRECTOR/A EJECUTIVO/A'),
  ('ENFERMERA/O', 'ENFERMERA/O'),
  ('ENFERMERA/O ESPECIALISTA', 'ENFERMERA/O ESPECIALISTA'),
  ('ESPECIALISTA ADMINISTRATIVO I', 'ESPECIALISTA ADMINISTRATIVO I'),
  ('ESPECIALISTA EN SALUD PUBLICA I', 'ESPECIALISTA EN SALUD PUBLICA I'),
  ('JEFE DE OFICINA', 'JEFE DE OFICINA'),
  ('JEFE DE ORGANO DE CONTROL INSTITUCIONAL', 'JEFE DE ORGANO DE CONTROL INSTITUCIONAL'),
  ('MEDICO', 'MEDICO'),
  ('MEDICO ESPECIALISTA', 'MEDICO ESPECIALISTA') ,
  ('NUTRICIONISTA', 'NUTRICIONISTA'),
  ('ODONTOLOGO', 'ODONTOLOGO'),
  ('PILOTO DE AMBULANCIA', 'PILOTO DE AMBULANCIA'),
  ('PSICOLOGO', 'PSICOLOGO'),
  ('QUIMICO FARMACEUTICO', 'QUIMICO FARMACEUTICO'),
  ('TECNICO ADMINISTRATIVO I', 'TECNICO ADMINISTRATIVO I'),
  ('TECNICO ADMINISTRATIVO III', 'TECNICO ADMINISTRATIVO III'),
  ('TECNICO ASISTENCIAL', 'TECNICO ASISTENCIAL'),
  ('TECNICO EN ARCHIVO', 'TECNICO EN ARCHIVO'),
  ('TECNICO EN ENFERMERIA', 'TECNICO EN ENFERMERIA'),
  ('TECNICO EN ENFERMERIA I', 'TECNICO EN ENFERMERIA I'),
  ('TECNICO EN FARMACIA I', 'TECNICO EN FARMACIA I'),
  ('TECNICO EN LABORATORIO I', 'TECNICO EN LABORATORIO I'),
  ('TECNICO EN NUTRICION I', 'TECNICO EN NUTRICION I'),
  ('TECNICO EN PLANIFICACION', 'TECNICO EN PLANIFICACION'),
  ('TECNICO EN REHABILITACION', 'TECNICO EN REHABILITACION'),
  ('TECNICO EN SERVICIOS GENERALES I', 'TECNICO EN SERVICIOS GENERALES I'),
  ('TECNICO ESPECIALIZADO', 'TECNICO ESPECIALIZADO'),
  ('TECNICO/A ADMINISTRATIVO/A II', 'TECNICO/A ADMINISTRATIVO/A II'),
  ('TECNOLOGO MEDICO', 'TECNOLOGO MEDICO'),
  ('TRABAJADOR DE SERVICIOS GENERALES', 'TRABAJADOR DE SERVICIOS GENERALES'),
  ('TRABAJADOR SOCIAL', 'TRABAJADOR DE SERVICIOS GENERALES')
)

niveles = (
  ('CD-I', 'CD-I'),
  ('CD-V', 'CD-V'),
  ('ENF-10', 'ENF-10'),  
  ('ENF-11', 'ENF-11'),
  ('ENF-12', 'ENF-12'),
  ('ENF-13', 'ENF-13'),
  ('ENF-14', 'ENF-14'),
  ('F-3', 'F-3'), 
  ('F-4', 'F-4'), 
  ('F-5', 'F-5'), 
  ('G5-V', 'G5-V'),
  ('MC-1', 'MC-1'),
  ('MC-2', 'MC-2'),
  ('MC-3', 'MC-3'),
  ('MC-4', 'MC-4'),
  ('MC-5', 'MC-5'),
  ('OPS-IV', 'OPS-IV'),
  ('OPS-V', 'OPS-V'),
  ('OPS-VIII', 'OPS-VIII'),
  ('PS-IV', 'PS-IV'),
  ('PS-V', 'PS-V'),
  ('PS-VI', 'PS-VI'),
  ('PS-VII', 'PS-VII'),
  ('PS-VIII', 'PS-VIII'),
  ('SAA', 'SAA'),
  ('SAB', 'SAB'),
  ('SAC', 'SAC'),
  ('SAD', 'SAD'),
  ('SAF', 'SAF'),
  ('SPC', 'SPC'),
  ('SPD', 'SPD'),
  ('SPE', 'SPE'),
  ('SPF', 'SPF'),
  ('STA', 'STA'),
  ('STB', 'STB'),
  ('STC', 'STC'),
  ('STD', 'STD'),
  ('STE', 'STE'),
  ('STF', 'STF'),
  ('TM-1', 'TM-1'),
  ('TM-2', 'TM-2'),
)

estados = (
  ('S', 'Soltero/a'),
  ('C', 'Casado/a')
)

sexo = (
  ('F', 'Femenino'),
  ('M', 'Masculino')
)

tipo_vinculo = (
  ('Nombramiento', 'Nombramiento'),
  ('Contrato', 'Contrato'),
  ('Adenda', 'Adenda'),
  ('Asignación de Funciones', 'Asignación de Funciones'),
  ('Destaque de otra Dependencia', 'Destaque de otra Dependencia'),
  ('Renovación de Destaque de otra Dependencia', 'Renovación de Destaque de otra Dependencia'),
  ('Destaque a otra Dependencia', 'Destaque a otra Dependencia'),
  ('Designación de otra Dependencia', 'Designación de otra Dependencia'),
  ('Designación a otra Dependencia', 'Designación a otra Dependencia'),
  ('Rotación', 'Rotación'), 
  ('Encargatura', 'Encargatura'),
  ('Renovación de Encargatura', 'Renovación de Encargatura'),
  ('Permuta', 'Permuta'),
  ('Ascenso', 'Ascenso'),
  ('Cambio de grupo Ocupacional', 'Cambio de grupo Ocupacional'),
  ('Otro', 'Otro'),
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

documento = (
  ('R.A.', 'Resolución Administrativa'),
  ('R.D.', 'Resolución Directoral'),
  ('Memorando', 'Memorando')
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

documentos_grado = [
  (10, "Secundaria Completa"),
  (20, "Superior Técnica Incompleta"),
  (30, "Superior Técnica"),
  (40, "Superior Universitario Incompleta"),
  (50, "Superior Universitario"),
  (60, "Maestría"),
  (70, "Doctorado"),
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

periodo_evaluacion = [
  ("I", "I"),
  ("II", "II"),
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

tipo_movimientos = [
  (10, "LSGH"),
  (20, "LCGH"),
]