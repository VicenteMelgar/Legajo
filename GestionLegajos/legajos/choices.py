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
  (5, 'Nombramiento'),
  (10, 'Reasignación'),
  (15, 'Contrato a plazo fijo'),
  (20, 'Destaque de otra Dependencia'),
  (25, 'Designación de otra Dependencia'),
)

tipo_compensacion = (
  (5, 'Por cumplir 25 años de Servicios'),
  (10, 'Por cumplir 30 años de Servicios'),
)

tipo_desplazamiento = (
  (5, 'Designación'),
  (10, 'Rotación'),
  (15, 'Destaque'),
  (20, 'Encargatura')
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
  (5, 'Resolución Administrativa'),
  (10, 'Resolución Directoral'),
  (15, 'Memorando')
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
  (39, "Declaración Jurada por Nepotismo"),
  (42, "Otros Documentos"),
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

documentos_prueba = [
  (3, "Evaluación y resultados del período de prueba"),
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
  (3, "Especialización"),
  (6, "Diplomado"),
  (9, "Congreso"),
  (12, "Convención"),
  (15, "Conferencia"),
  (18, "Curso de capacitación"),
  (21, "Seminario"),
  (24, "Simposio"),
  (27, "Charla"),
  (30, "Taller"),
  (33, "Certificado"),
  (36, "Constancia"),
]

documentos_experiencia = [
  (3, "Certificado"),
  (6, "Constancia"),
  (9, "Resolución"),
  (12, "Memorando"),
]

documentos_retencion = [
  (5, "Exoneración de retención de cuarta categoría"),
  (10, "Exoneración de retención de quinta categoría"),
  (15, "Liquidación de beneficios sociales"),
  (20, "Pago de compensación económica"),
]

documentos_evaluacion = [
  (5, "Factores de evaluación"),
  (10, "Registro de evidencias"),
  (15, "Formato de reunión de seguimiento"),
  (20, "Notificación de evaluación obtenida"),
  (25, "Acta de retroalimentación de resultados de desempeño"),
  (30, "Plan de mejora"),
]

documentos_reconocimientos = [
  (5, "Reconocimiento"),
  (10, "Sanción"),
]

documentos_laboral = [
  (5, "Controversias Individuales"),
  (10, "Controversias Colectivas"),
  (15, "Afiliación al Sindicato"),
]

documentos_sst = [
  (5, "Cargo de entrega del Reglamento de SST"),
  (10, "Registro de entrenamiento, y simulacros de emergencias"),
  (15, "Capacitaciones brindadas por la entidad"),
  (20, "Trámites y gestiones de seguro"),
  (25, "Trámites y gestiones de subsidios"),
  (30, "Descanso Médico"),
  (35, "Afiliaciones a Entidades Prestadoras de Salud (EPS)"),
]

documentos_desvinculacion = [
  (5, "Resolución de término de designación"),
  (10, "Resolución de término del servicio civil de carrera"),
  (15, "Memorando  de término de vínculo del servicio civil"),
  (20, "Informe de Gestión"),
  (25, "Entrega de cargo/puesto"),
  (30, "Liquidación de beneficios sociales y/o pensión"),
  (35, "Carta de no renovación de contrato a plazo determinado"),
]

motivo_progresion = [
  (5, "Ascenso"),
  (10, "Cambio de grupo Ocupacional"),
]

tipo_movimientos = [
  (5, "LSGH"),
  (10, "LCGH"),
]