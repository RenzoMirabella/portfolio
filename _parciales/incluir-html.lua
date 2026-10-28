-- Inserta un fragmento HTML (las figuras de _figuras/) donde haya un div con el atributo
-- incluir="archivo.html". Corre después de freeze, así que reconstruir una figura no obliga a
-- volver a ejecutar el Python de la página.
function Div(el)
  local archivo = el.attributes["incluir"]
  if not archivo then return nil end
  local dir = pandoc.path.directory(quarto.doc.input_file)
  local f = io.open(pandoc.path.join({ dir, archivo }), "r")
  if not f then
    quarto.log.warning("No encontré " .. archivo)
    return nil
  end
  local html = f:read("a")
  f:close()
  return pandoc.RawBlock("html", html)
end
