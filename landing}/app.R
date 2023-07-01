library(shiny)

# Define the User Interface
ui <- navbarPage("Ye, ye, ye ye.",
                 tabPanel("Inicio",
                          fluidRow(
                            column(3),
                            column(6,
                                   # A header for our landing page
                                   tags$br(),
                                   tags$br(),
                                   h1("Bienvenido a Chatbunny", align = "center"),
                                   
                                   # A brief description
                                   
                                   # A call-to-action button
                                   actionButton("cta", "Chatea con Bad Bunny.", class = "btn btn-primary btn-lg active", width = "100%"),
                                   tags$style(".btn { margin-top: 100px; }"),
                                   tags$script(HTML("$(document).on('click', '#cta', function(){window.location.href = 'http://www.google.com';});"))
                            ),
                            column(3)
                          )
                 ),
                 tabPanel("Acerca de nosotros",
                          # The About page content can be added here
                          fluidRow(
                            column(3),
                            column(6,
                                   h2("Acerca de nosotros", align = "center"),
                                   p("Somos muy buenos.")
                            ),
                            column(3)
                          )
                 )
)

# Define the Server function
server <- function(input, output) {
  observeEvent(input$cta, {
    showModal(modalDialog(
      title = "Congratulations!",
      "You're one step closer to experiencing ChatBunny. We'll be in touch shortly."
    ))
  })
}

# Run the application 
shinyApp(ui = ui, server = server)